import numpy, Image, math, sys
import num_constants

def rand_array(width, height):
    return numpy.random.rand(width, height, 3)

def parse_rgb(pi, idx):
    end_idx = idx + 9
    interest = pi[idx:end_idx]
    r = interest[0:3]
    g = interest[3:6]
    b = interest[6:]
    color = (int(r), int(g), int(b))
    return color, end_idx

def calc_block_size(w, h):
    pixels = w * h
    digits_needed = pixels * 9
    blocks = digits_needed / num_constants.NUM_DIGITS
    return int(math.ceil(blocks))

def make_horline_pi_image(pi, g, w, h):
    pi_loc = 0
    block_size = calc_block_size(w, h) * g

    a = rand_array(w, h)
    for i in xrange(w):
        for j in xrange(h):
            if ((i + j) % block_size == 0):   # got a new block of fancy colors fellas
                col, pi_loc = parse_rgb(pi, pi_loc)
            a[i][j] = col

    img = Image.fromarray(a.astype('uint8')).convert('RGBA')
    return img

def make_verline_pi_image(pi, g, w, h):
    pi_loc = 0
    block_size = calc_block_size(w, h) * g

    a = rand_array(w, h)
    for i in xrange(w):
        for j in xrange(h):
            if (i % block_size == 0):
                col, pi_loc = parse_rgb(pi, pi_loc)
            else:
                col = a[i-1][j]
            a[i][j] = col

    img = Image.fromarray(a.astype('uint8')).convert('RGBA')
    return img

def make_square_pi_image(pi, g, w, h):
    pi_loc = 0
    block_size = calc_block_size(w, h) * g
    row_size = int(math.ceil(math.sqrt(block_size)))

    calc_color = True
    a = rand_array(w, h)
    for i in xrange(w/row_size):
        for j in xrange(h/row_size):
            col, pi_loc = parse_rgb(pi, pi_loc)

            ri = i * row_size
            rj = j * row_size
            for x in xrange(ri, ri+row_size):
                for y in xrange(rj, rj+row_size):
                    a[x][y] = col

    img = Image.fromarray(a.astype('uint8')).convert('RGBA')
    return img

def get_next_arg(argmap, arg):
    loc = argmap[arg] + 1
    na = sys.argv[loc]
    return na

def build_argmap():
    argmap = {}
    for i in range(1, len(sys.argv)):
        argmap[sys.argv[i]] = i
    return argmap

def main():
    argmap = build_argmap()

    if '-size' in argmap:
        size = int(get_next_arg(argmap, '-size'))
    else:
        size = 300

    styles = {
        'hor': make_horline_pi_image,
        'ver': make_verline_pi_image,
        'square': make_square_pi_image
    }
    if '-style' in argmap:
        style_arg = get_next_arg(argmap, '-style')
    else:
        style_arg = 'hor'
    image_styler = styles[style_arg]

    numbers = {
        'pi': num_constants.PI,
        'e': num_constants.E,
        'tau': num_constants.TAU,
        'phi': num_constants.PHI,
        'sq2': num_constants.SQ2
    }
    if '-num' in argmap:
        num_arg = get_next_arg(argmap, '-num')
    else:
        num_arg = 'pi'
    number = numbers[num_arg]

    if '-grain' in argmap:
        grain = int(get_next_arg(argmap, '-grain'))
    else:
        grain = 1

    img = image_styler(number, grain, size, size)
    name = style_arg + '_' + str(size) + '_' + str(grain) + 'grain_' + num_arg + '.jpg'
    img.save(name)

if __name__ == '__main__':
    main()