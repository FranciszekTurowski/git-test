import sys
successful_requests = 0
failed_requests = 0

try:
    with open('server_logs.txt') as file:
        for line in file:
            date, time, ip, status_code = line.split()
        
        
            if 200 <= int(status_code) <= 299:
                successful_requests+=1
            elif 400 <= int(status_code) <= 599:
                failed_requests+=1
except FileNotFoundError:
    print("Plik z logami nie został znaleziomy") 
    sys.exit()  
    
with open("report.txt",'w') as file:
        file.write(f'succesful_requests: {successful_requests}\n')   
        file.write(f'failed_requests: {failed_requests}\n')    
