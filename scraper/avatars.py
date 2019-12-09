import rest
import output
import champs


API_URL = 'https://www.mobafire.com/images/champion/square/{champion}.png'


def _get_champ_avi(outpt, champ):
    res = rest.get_image(API_URL.format(champion=champ))
    output.output_chunked_file(outpt, '{}.png'.format(champ), res)


def exec(args):
    chmps = []

    if args.champions is not None:
        chmps = args.champions.split(',')
    else:
        chmps = [c['id'] for c in champs.get_champs(args)]

    for c in chmps:
        _get_champ_avi(args.output, c)
