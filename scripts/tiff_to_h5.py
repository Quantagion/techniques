from skimage.io import imread
import dask.array as da
import h5py


def main():
    tiff_path = 'C:/users/email/documents/test/tiff_image.tif'
    h5_path = 'C:/users/email/documents/test/h5_image.h5'
    tiff = imread(tiff_path)
    
    print(tiff.shape)
    print(tiff.dtype)
    
    # to h5
    with h5py.File(h5_path, 'w') as h5:
        out = h5.require_dataset('/x',
                                shape=tiff.shape,
                                dtype=tiff.dtype)
        out[:, :, :] = tiff
    
    # and from h5
    with h5py.File(h5_path, 'r') as h5:
        print("KEY NAMES:", h5.keys())
        print()
        
        only_key = list(h5.keys())[0]
        h5_data =h5[only_key]
        
        print(h5_data[:5])
    
    
if __name__ == '__main__':
    main()