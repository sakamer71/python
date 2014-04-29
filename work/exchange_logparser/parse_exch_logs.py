__author__ = 'skamer'
import MySQLdb
from os import path,listdir
dirpath = ['c:/tmp/exchglogs3/mspht01/','c:/tmp/exchglogs3/mspht02/']
from mysql_connect import db,cursor
# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")
#cursor.execute("select count(*) from logs")
# Fetch a single row using fetchone() method.
data = cursor.fetchone()
filelist = []
table = 'logs'
print "Database version : %s " % data


def locate_logs(dir,filelist):
    filenames = listdir(dir)
    #print "the list of files in dir {} is {}".format(dir,filenames)
    for filename in filenames:
        if path.isfile(path.join(dir,filename)):
            filelist.append(path.join(dir,filename))
    return filelist

for d in dirpath:
    myfilelist = locate_logs(d,filelist)
    print "myfilelist is {}".format(myfilelist)

## poc can i open the file... yes i can
#print first log
fh=open(filelist[0])

def format_file(myfile):
    #newfile = 'staging.txt'
    fh = open(myfile)
    newfile = open('staging.txt', 'w')
    for line in fh:
        if not line.startswith('#'):
            #if not line.startswith('#Software: Microsoft Exchange Server'):
            newfile.write(line)


def insert_csv_to_sql(cursor,filelist,table):
    sql  = "load data local infile '{}' "
    sql += "into table {} "
    sql += "fields terminated by ',' "
    sql += "lines terminated by '\n' "
    sql += "ignore 5 lines "
    sql += "(datetime, clientip, clienthostname, serverip, serverhostname, sourcecontext, connectorid, "
    sql += "source, eventid, internalmessageid, messageid, recipientaddress, recipientstatus, "
    sql += "totalbytes, recipientcount, relatedrecipientaddress, reference, messagesubject, "
    sql += "senderaddress,returnpath,messageinfo); "


    for file in filelist:
        print "now importing {}".format(file)
        print "my sql command is {}".format(sql.format(file,table))
        cursor.execute(sql.format(file,table))
        print "Success!"
        db.commit()
        #except Exception:
            # Rollback in case there is any error
         #   print "Error - rolling back {}".format(file)
          #  db.rollback()

testlist = filelist[0:3]
#testlist = filelist
#print "my test list is \n{}".format(testlist)

print "importing {}".format(testlist)
#insert_csv_to_sql(cursor,testlist,table)
insert_csv_to_sql(cursor,filelist,table)
db.close()