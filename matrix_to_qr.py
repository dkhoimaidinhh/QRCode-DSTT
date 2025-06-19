import qrcode
from PIL import Image

# Example matrix input (0s and 1s)
# Replace this with your own matrix
def matrix_to_qr(matrix, output_file='qr_from_matrix.png'):
    # Convert matrix to string data for QR code
    data = '\n'.join([''.join(map(str, row)) for row in matrix])
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"QR code saved as {output_file}")

def link_to_qr(link, output_file='qr_from_link.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"QR code for link saved as {output_file}")

if __name__ == "__main__":
    # Generate a 21x21 matrix with a checkerboard pattern
    matrix = [[(i + j) % 2 for j in range(21)] for i in range(21)]
    matrix_to_qr(matrix)

    # Generate QR code for the provided Facebook link
    link = "https://www.facebook.com/anh.quynh.558366"
    link_to_qr(link)
