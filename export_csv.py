from os import listdir
from os.path import isfile, join
from skimage import io

def read_image(path):
    img = io.imread(path, as_gray=True)
    return list(img.flatten())

def get_id(path):
    return int(path.split('/')[-1].split('.')[0].split('_')[0])

def export_folder(folder_path, input_format = '.png'):
    for folder in listdir(folder_path):
        print(folder)
        files = [f for f in listdir(join(folder_path, folder)) if isfile(join(folder_path, folder, f)) and f.endswith(input_format)]
        print(files)
        with open(folder_path + '.csv', 'a+') as out:
            for f in files:
                path = join(folder_path, folder, f)
                id = get_id(path)
                data = read_image(path)
                data.insert(0, id)
                str_data = [str(x) for x in data]
                out.write(','.join(str_data) + '\n')

def export_csv():
    for folder in listdir('python/images_background'):
        export_folder(join('python/images_background', folder))
    for folder in listdir('python/images_background 2'):
        export_folder(join('python/images_background 2', folder))
    for folder in listdir('python/images_background_small1'):
        export_folder(join('python/images_background_small1', folder))
    for folder in listdir('python/images_background_small2'):
        export_folder(join('python/images_background_small2', folder))

if __name__ == "__main__":
    export_csv()
