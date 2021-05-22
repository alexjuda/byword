import datamuse


def get_synonyms(query: str):
    dm = datamuse.Datamuse()
    return [res["word"] for res in dm.words(ml=query)][:10]
