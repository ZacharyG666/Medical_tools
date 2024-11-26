import SimpleITK as sitk

def get_image_metadata(image_path):
    # 读取图像
    image = sitk.ReadImage(image_path)
    
    # 获取图像的尺寸
    image_size = image.GetSize()
    
    # 获取体素大小
    image_spacing = image.GetSpacing()
    
    # 获取图像原点
    image_origin = image.GetOrigin()
    
    # 获取图像方向
    image_direction = image.GetDirection()
    
    # 构建元信息字典
    metadata = {
        'Size': image_size,
        'Spacing': image_spacing,
        'Origin': image_origin,
        'Direction': image_direction
    }
    
    return metadata

def print_metadata(metadata):
    print("Image Metadata:")
    print("Size:", metadata['Size'])
    print("Spacing (voxel size):", metadata['Spacing'])
    print("Origin:", metadata['Origin'])
    print("Direction:", metadata['Direction'])

def main(image_path):
    metadata = get_image_metadata(image_path)
    print_metadata(metadata)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_image>")
    else:
        main(sys.argv[1])