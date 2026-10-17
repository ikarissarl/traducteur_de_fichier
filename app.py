from pathlib import Path
from uuid import uuid4
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from traduction import (Traducteur_csv, Traducteur_json, Traducteur_sql,
                        Traducteur_netcdf4, Traducteur_parquet)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

DOSSIER = Path(app.root_path) / "temp"
DOSSIER.mkdir(exist_ok=True)

SOURCES = {
    "csv": {"extensions": [".csv"], "traducteur": Traducteur_csv()},
    "json": {"extensions": [".json"], "traducteur": Traducteur_json()},
    "sql": {"extensions": [".db", ".sqlite", ".sqlite3"], "traducteur": Traducteur_sql()},
    "netcdf": {"extensions": [".nc"], "traducteur": Traducteur_netcdf4()},
    "parquet": {"extensions": [".parquet"], "traducteur": Traducteur_parquet()},
}

FORMATS = {
    "csv": ".csv", "json": ".json", "jsonline": ".jsonl", "excel": ".xlsx",
    "xml": ".xml", "html": ".html", "parquet": ".parquet", "feather": ".feather",
    "orc": ".orc", "hdf5": ".h5", "sql": ".db", "stata": ".dta",
    "tsv": ".tsv", "markdown": ".md", "latex": ".tex",
}

CONVERSIONS = {source: [f for f in FORMATS if f != source] for source in SOURCES}


def detecter_format(extension):
    for nom_format, infos in SOURCES.items():
        if extension in infos["extensions"]:
            return nom_format
    return None


def afficher(erreur=None):
    page = render_template(
        "index.html",
        sources={n: i["extensions"] for n, i in SOURCES.items()},
        conversions=CONVERSIONS,
        formats=FORMATS,
        accept=",".join(e for i in SOURCES.values() for e in i["extensions"]),
        erreur=erreur,
    )
    return page, (400 if erreur else 200)


@app.route("/", methods=["GET", "POST"])
def accueil():
    if request.method == "GET":
        return afficher()

    fichier = request.files.get("fichier")
    choisi = request.form.get("choisi")
    cible = request.form.get("cible")
    table = request.form.get("table", "").strip() or "donnees"
    nom = secure_filename(request.form.get("nom", "")) or "resultat"

    if not fichier or fichier.filename == "":
        return afficher("Choisis un fichier à téléverser.")
    if choisi not in SOURCES or cible not in FORMATS:
        return afficher("Choisis le format de ton fichier et le format de destination.")
    if choisi == cible:
        return afficher("Le format de départ et le format de destination sont identiques.")
    if not table.isidentifier():
        return afficher("Nom de table invalide : lettres, chiffres et _ seulement.")

    extension = Path(fichier.filename).suffix.lower()
    trouve = detecter_format(extension)
    if trouve is None:
        return afficher(f"L'extension {extension or '(aucune)'} n'est pas reconnue comme étant un fichier {choisi}.")
    if trouve != choisi:
        return afficher(f"Votre fichier n'est pas un {choisi} mais un {trouve}.")

    traducteur = SOURCES[choisi]["traducteur"]
    entree = DOSSIER / f"{uuid4().hex}{extension}"
    sortie = DOSSIER / f"{uuid4().hex}{FORMATS[cible]}"
    fichier.save(entree)

    try:
        methode = getattr(traducteur, f"{choisi}_{cible}")
        if choisi == "sql" or cible == "sql":
            document = methode(entree, table, sortie)
        else:
            document = methode(entree, sortie)
    except Exception as erreur:
        return afficher(f"La conversion a échoué : {erreur}")
    finally:
        entree.unlink(missing_ok=True)

    return render_template(
        "retour.html",
        identifiant=document.name,
        nom=nom + FORMATS[cible],
        source=choisi,
        cible=cible,
    )


@app.route("/telecharger/<identifiant>")
def telecharger(identifiant):
    nom = secure_filename(request.args.get("nom", "")) or "resultat"
    return send_from_directory(DOSSIER, identifiant,
                               as_attachment=True, download_name=nom)


if __name__ == "__main__":
    app.run(debug=True)