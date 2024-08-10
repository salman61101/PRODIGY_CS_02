from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path):
    
    img = Image.open(input_path)
    img = img.convert('RGB')  

    
    img_array = np.array(img)

    
    encrypted_array = img_array.copy()
    encrypted_array[:, :, 0], encrypted_array[:, :, 2] = img_array[:, :, 2], img_array[:, :, 0]

    
    encrypted_img = Image.fromarray(encrypted_array)

    
    encrypted_img.save(output_path)
    print(f'Encrypted image saved as {output_path}')

def decrypt_image(input_path, output_path):

    img = Image.open(input_path)
    img = img.convert('RGB')  

    
    img_array = np.array(img)

    
    decrypted_array = img_array.copy()
    decrypted_array[:, :, 0], decrypted_array[:, :, 2] = img_array[:, :, 2], img_array[:, :, 0]

    
    decrypted_img = Image.fromarray(decrypted_array)

    
    decrypted_img.save(output_path)
    print(f'Decrypted image saved as {output_path}')

input_image_path = 'input.png'
encrypted_image_path = 'encrypted.png'
decrypted_image_path = 'decrypted.png'


encrypt_image(input_image_path, encrypted_image_path)

decrypt_image(encrypted_image_path, decrypted_image_path)
