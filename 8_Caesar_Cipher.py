alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# def encrypt(original_text,shift_amount):
#     cipher_text=""
#     for letter in original_text:
#         shifted_position=alphabet.index(letter)+shift_amount
#         shifted_position%=len(alphabet)
#         cipher_text+=alphabet[shifted_position]
#     print(f"Here is the encoded results : {cipher_text}")

# encrypt(original_text=text,shift_amount=shift)


# def decrypt(original_text,shift_amount):
#     decoded_text=""
#     for letter in original_text:
#         shifted_position=alphabet.index(letter)-shift_amount
#         shifted_position%=len(alphabet)
#         decoded_text+=alphabet[shifted_position]
#     print(f"Here is the decoded result : {decoded_text}")


def caesar(original_text,shift_amount,encode_or_decode):
    output_text=""
    if encode_or_decode=="decode":
                shift_amount*=-1
    for letter in original_text:
        if letter not in alphabet:
            output_text+=letter
        else:
            shifted_position=alphabet.index(letter)-shift_amount
            shifted_position%=len(alphabet)
            output_text+=alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result : {output_text}")


should_continue=True
while should_continue:
    direction=input("Type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()
    text=input("Type your secret message: \n").lower()
    shift=int(input("Type your shift number : \n"))

    caesar(original_text=text, shift_amount=shift,encode_or_decode=direction)
    restart=input("Type 'yes' if you want to go again. Otherwise type 'no' :\n").lower()
    if restart=="no":
        should_continue=False
        print("GoodBye!")


