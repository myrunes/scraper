import rest
import output


API_URL = 'https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json'


EXCEPTIONS = {
    'Nunu & Willump': 'nunu'
}


def _get_champ_id(name):
    if name in EXCEPTIONS:
        return EXCEPTIONS[name]
    return name.replace(' ', '-').replace('\'', '').replace('.', '').lower()


def get_champs(args):
    raw = rest.get_json(API_URL.format(version=args.patch))
    champs = []
    for k, v in raw['data'].items():
        name = v['name']
        champs.append({
            'id': _get_champ_id(name),
            'name': name
        })
    return champs


def exec(args):
    champs = get_champs(args)
    output.output_json(args.output, 'champs.json', champs)
