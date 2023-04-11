import nfc 

def on_connect(tag):
    
  print(tag)
  
  # タグのIDなどを出力する
  if isinstance(tag, nfc.tag.tt3.Type3Tag):
    try:
      # 内容を16進数で出力する
     print('  ' + '\n  '.join(tag.dump()))
     
    except Exception as e:
     print("error: %s" % e)
     
  else:
    print( "error: tag isn't Type3Tag")

def main():
  with nfc.ContactlessFrontend('usb') as clf:
    clf.connect(rdwr={'on-connect': on_connect})

if __name__ == '__main__':
  main()
