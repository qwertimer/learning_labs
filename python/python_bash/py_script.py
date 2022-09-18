import sys; ip = f"{sys.argv[1]}"; ip_out = f"{'.'.join(ip.split('.')[:-1])}.0"; print(ip_out);
