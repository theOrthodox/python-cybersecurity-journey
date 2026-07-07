import requests

url=input("please enter the file path of the url lists ")

def url_checker(url):
    try:
        with open(url) as extracter:
            list_url=extracter.readlines()
    except FileNotFoundError:
        print("Entered FIle is not available")
        return
    
    counts ={
        "count" : 0,
        "2xx" : 0,
        "4xx" : 0,
        "5xx" : 0,
        "failed" : 0
    }

    for urls in list_url:
        urls=urls.strip()
        print(f"Checking : {urls}")
        counts["count"] +=1
        try:
            r=requests.get(urls,timeout=10)
            print("===== Report =====")
            print(f"Original URL :{urls}")
            print(f"Final URL :{r.url}")
            print(f"STATUS CODE :{r.status_code}")
            print(f"RESPONSE TIME :{r.elapsed.total_seconds()*1000:.2f}ms")
            print(f"REDIRECTION :{bool(r.history)}")
            if r.status_code >= 200 and  r.status_code < 300:
                    counts["2xx"] +=1
            elif r.status_code >=400 and r.status_code < 500:
                    counts["4xx"] +=1
            elif r.status_code >=500 and r.status_code <600:
                    counts["5xx"] +=1
            if r.history:
                 print(f"Redirected from :{r.history[0].url}")
                 print(f"redirected to :{r.url}")
        except requests.exceptions.RequestException as e:
            print(e)
            counts["failed"] +=1


        print("===== ===== =====")
        
    print("===== TOTAL SUMMARY REPORT =====")
    print(f"total checked :{counts.get('count')}")
    print(f"total with 2xx code :{counts.get('2xx')}")
    print(f"total with 4xx code :{counts.get('4xx')}")
    print(f"total with 5xx code :{counts.get('5xx')}")
    print(f"total failed counts :{counts['failed']}")

        
url_checker(url)
