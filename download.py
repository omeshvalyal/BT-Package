import urllib.request

url = "https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.85/bin/apache-tomcat-9.0.85.tar.gz"
destination = "apache-tomcat-9.0.85.tar.gz"

try:
    print("Downloading", url)
    urllib.request.urlretrieve(url, destination)
    print("Download complete!")
except Exception as e:
    print("Error:", e)
