import base64
import os
class single:
    def encode(dta, debug=False):
        
        dta = dta.encode("utf-8")
       
        dta = base64.b16encode(dta)
        if debug:
            print("16 done")
        dta = base64.b32encode(dta)
        if debug:
            print("32 done")
        dta = base64.b64encode(dta)
        if debug:
            print("64 done")
        dta = base64.b85encode(dta)
        if debug:
            print("85 done")
        
        dta = dta.decode("utf-8") 
        return dta 
    def decode(dta, debug=False):
        all_done = False
        while all_done == False:
            dta = dta.encode("utf-8")
            try:
                dta = base64.b85decode(dta)
                eightFiveDone = True
                if debug:
                    print("85 done")
            except ValueError:
                eightFiveDone = False
                if debug:
                    print("Value not 85")
            try:
                dta = base64.b64decode(dta)
                sixFourDone = True
                if debug:
                    print("64 done")
            except ValueError:
                sixFourDone = False
                if debug:
                    print("Value not 64")
            try:
                dta = base64.b32decode(dta)
                threeTwoDone = True
                if debug:
                    print("32 done")
            except ValueError:
                threeTwoDone = False
                if debug:
                    print("Value not 32")
            try:
                sixteenDone = True
                dta = base64.b16decode(dta)
                if debug:
                    print("16 done")
            except ValueError:
                sixteenDone = False
                if debug:
                    print("Value not 16")
            if eightFiveDone == False and sixFourDone == False and threeTwoDone == False and sixteenDone == False:
                pass
            else:


        
                dta = dta.decode("utf-8") 
                return dta
            break
                
        
"""class defined:
       def encode(dta, vl, debug=False):
        
        dta = dta.encode("utf-8")
        while vl != 0:
            dta = base64.b16encode(dta)
            if debug:
                print("16 done")
            dta = base64.b32encode(dta)
            if debug:
                print("32 done")
            dta = base64.b64encode(dta)
            if debug:
                print("64 done")
            dta = base64.b85encode(dta)
            if debug:
                print("85 done")
            vl = vl - 1
            if debug:
                print(f"Defined encodings left:{vl}")
        dta = dta.decode("utf-8")
        return dta
       def decode(dta, vl, debug=False):
        
        dta = dta.encode("utf-8")
        while vl != 0:
            dta = base64.b16decode(dta)
            if debug:
                print("16 done")
            dta = base64.b32decode(dta)
            if debug:
                print("32 done")
            dta = base64.b64decode(dta)
            if debug:
                print("64 done")
            dta = base64.b85decode(dta)
            if debug:
                print("85 done")
            vl = vl - 1
            if debug:
                print(f"Defined decodings left:{vl}")
        dta = dta.decode("utf-8")
        return dta        
    

    def encode(dta, debug=False):
        vl = 10
        dta = dta.encode("utf-8")
        while vl != 0:
            dta = base64.b16encode(dta)
            if debug:
                print("16 done")
            dta = base64.b32encode(dta)
            if debug:
                print("32 done")
            dta = base64.b64encode(dta)
            if debug:
                print("64 done")
            dta = base64.b85encode(dta)
            if debug:
                print("85 done")
            vl = vl - 1
            if debug:
                print(f"Safe encodings left:{vl}")
        dta = dta.decode("utf-8")
        return dta    
    def encode(dta, debug=False):
        vl = 10
        dta = dta.encode("utf-8")
        while vl != 0:
            dta = base64.b16decode(dta)
            if debug:
                print("16 done")
            dta = base64.b32decode(dta)
            if debug:
                print("32 done")
            dta = base64.b64decode(dta)
            if debug:
                print("64 done")
            dta = base64.b85decode(dta)
            if debug:
                print("85 done")
            vl = vl - 1
            if debug:
                print(f"Safe decodings left:{vl}")
        dta = dta.decode("utf-8")
        return dta
       """
