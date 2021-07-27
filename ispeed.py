import speedtest
test=speedtest.Speedtest()

test.get_servers()#list of server
best=test.get_best_server()#best server available
print("Available best server :")
#testing download
download_result=test.download()
print(f"Download speed:{download_result/1024/1024:.2f} Mbit/s")
#upload
upload_result=test.upload()
print(f"Upload speed:{upload_result/1024/1024:.2f} Mbit/s")
#ping issue
pingres=test.results.ping
print(f"ping :{pingres:.2f} ms")