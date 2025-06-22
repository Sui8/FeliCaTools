import nfc
    
service_code_9 = 0x0009
service_code_b = 0x000b
    
def on_connect(tag):
  print("Connected")
  # タグのIDなどを出力する
  print(str(tag))
    
  if isinstance(tag, nfc.tag.tt3.Type3Tag):
    try:
      # ブロック0番の内容を16進数[bb]で書き込み、読み出す。
      sc = nfc.tag.tt3.ServiceCode(service_code_9 >> 6, service_code_9 & 0x3f)
      bc = nfc.tag.tt3.BlockCode(5, service=0)
      # data = 16 * "\xcc"
      data = tag.write_without_encryption([sc], [bc], bytearray(16))
      print(("block{0}: {1}".format( 0, binascii.hexlify(tag.read_without_encryption([sc_9], [bc])))))

    except Exception as e:
      print(f"Error: {e}")
  else:
    print("Error: Tag isn't Type3Tag")
    
# タッチ時のハンドラを設定して待機する
def main():
  print("Program has started!")
  with nfc.ContactlessFrontend("usb") as clf:
    clf.connect(rdwr={"on-connect":on_connect})

if __name__ == "__main__":
  main()
