def egcd(a, b): 
  x,y, u,v = 0,1, 1,0
  while a != 0: 
    q, r = b//a, b%a 
    m, n = x-u*q, y-v*q 
    b,a, x,y, u,v = a,r, u,v, m,n 
  gcd = b 
  return gcd, x, y 

def modinv(a, m): 
  gcd, x, y = egcd(a, m) 
  if gcd != 1: 
    return None 
  else: 
    return x % m 
 
def encrypt(text, key): 
  # Enkripsi = (a*x + b) % 26 
  return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in text.upper().replace(' ', '') ]) 


def decrypt(cipher, key): 
  # Dekripsi (E) = (a^-1*(E - b)) % 26
  return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher ]) 

def main(): 
  text = 'SYAUQI NUR HIBATULLAH'
  key = [3, 5] 

  # Memanggil fungsi enkripsi
  enc_text = encrypt(text, key) 

  print('Encrypted Text: {}'.format(enc_text)) 

  # Memanggil fungsi dekripsi 
  print('Decrypted Text: {}'.format(decrypt(enc_text, key) )) 


if __name__ == '__main__': 
  main() 