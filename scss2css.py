import sass

if __name__ == '__main__':
    res = sass.compile(filename='scss/style.scss', output_style='compressed')
    # res = sass.compile(filename='scss/style.scss')
    with open('static/style.min.css', 'w') as f:
        f.write(res)