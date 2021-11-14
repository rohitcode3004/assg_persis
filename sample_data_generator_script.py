"""To run this file, open the terminal , go to the folder location and type 
>python3 sample_data_generator_script.py
It will ask for the input in number form.
"""
import random
import string
import pymysql #use "sudo apt-get install python3-pymysql" to import it

def generate_router_data(n):
    list1 = []
    new_list =[]
    alphabets = "".join(set(string.ascii_lowercase))
    def generate_word(length):
        word = ""
        for i in range(length):
            word += random.choice(alphabets)
        return ("www."+word+".com")

    for i in range(n):
        sapid = "sapid_"+str(random.randint(10000, 100000))
        hostname = generate_word(random.randint(5,10))
        loopback = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        mac_address = "52:54:00:%02x:%02x:%02x" % (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
                )
        list1.append(sapid)
        list1.append(hostname)
        list1.append(loopback)
        list1.append(mac_address)
        new_list.append(tuple(list1))
        list1 *=0
    return new_list



if __name__ == '__main__':
	n = int(input("Enter a number to generate the data :")) 
	router_data = generate_router_data(n) 
	print("Data has been generated. Now, updating the database...") 

	dbhost="localhost"	
	dbuser="root"			#change the database username here
	dbpwd="12qwaszx"		#change the database password here
	dbdatabase="minitask" 
	 
	try:
		connection = pymysql.connect(dbhost,dbuser,dbpwd,dbdatabase)
		cursor = connection.cursor()

		# Prepare SQL query to INSERT a record into the database. 

		for item in router_data:
			query = """INSERT INTO accounts_router(sapid, hostname, loopback, mac_address) VALUES (%s, %s, %s, %s) """
			values = (item)
			cursor.execute(query,values)
			connection.commit()
		print("Database has been updated Successfully.")
	except Error as e:
		print('Error : ', e)
		connection.rollback() 
	finally: 
		# disconnect from server
		print("Closing the script now.") 
		connection.close()  
 
 
