import nfc 
import binascii
import time
import logging

syscode = 0xFE00
svccode = 0x39C9
logging.basicConfig()
# logging.getLogger("nfc").setLevel(logging.DEBUG-1)

def on_connect(tag):
  print("Connected")
  print(str(tag))
  
  if isinstance(tag,nfc.tag.tt3.Type3Tag):
    tag.idm, tag.pmm = tag.polling(system_code=syscode)
    tag.sys=syscode
    
    try:
      sc = nfc.tag.tt3.ServiceCode(svccode >> 6, svccode & 0x3F)
      bc = nfc.tag.tt3.BlockCode(2)
      data = tag.write_without_encryption([sc], [bc], bytearray(16))
      print("Wrote")
  
    except Exception as e:
      print(f"Error: {e}")
  else:
    print("Error: Not Type3Tag")

  return True 

def main():
  print("Program has started!")
  with nfc.ContactlessFrontend("usb") as clf:
    clf.connect(rdwr={"on-connect":on_connect})

if __name__=="__main__":
  main()
