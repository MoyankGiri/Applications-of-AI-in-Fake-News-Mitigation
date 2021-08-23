from PIL import Image, ImageChops, ImageEnhance


def ErrorLevelAnalysis(path, quality):
    filename = path
    
    im = Image.open(filename).convert('RGB')
    im.save(path, 'JPEG', quality=quality,optimize=True)
    resaved_im = Image.open(path)
    
    ela_im = ImageChops.difference(im, resaved_im)
    
    extrema = ela_im.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1
    scale = 255.0 / max_diff
    
    ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)
    
    return ela_im