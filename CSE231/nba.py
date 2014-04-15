__author__ = 'skamer'

## takes list of data on nba players
## uses formula to determine efficiency
## prints out the following:
####1. top 10 most efficient players
####FUTURE 2. The player who played the most minutes
####FUTURE 3. The player who played the most games
####FUTURE 4. The player who scored the most points
####FUTURE 5. The player who got the most rebounds
####FUTURE 6. The player who got the most penalties
####FUTURE 7. The player who made the most freethrows

from csv import reader
datafile = reader(open('players.csv'))
header=datafile.next()
efficiency_fields = ['firstname','lastname','pts','reb','asts','stl','blk','fga','fgm','fta','ftm','turnover','gp','minutes']
eff_dict={}
player_efficiency={}
player_gamesplayed={}

topnum = 30  #how many top players to list

##print header
## determine which field in the csv corresponds to each needed statistic
for field in efficiency_fields:
    eff_dict.update({field:header.index(field)})

#print eff_dict
def calc_efficiency(h,datarow):
    global player_efficiency
    #update list inline - set all null values to 0
    datarow = [ 1 if (x == 'NULL' or x == 'N') else x for x in datarow]
    eff = (1.0* (int(datarow[h['pts']]) + int(datarow[h['reb']]) + int(datarow[h['asts']]) +
                 int(datarow[h['stl']]) + int(datarow[h['blk']]) ) -
           ( (int(datarow[h['fga']]) - int(datarow[h['fgm']])) +
             (int(datarow[h['fta']]) - int(datarow[h['ftm']])) + int(datarow[h['turnover']]) ) ) / \
          int(datarow[h['gp']])
    lastname = datarow[h['lastname']]
    firstname = datarow[h['firstname']]
    myname="%s %s" %(firstname,lastname)
    #*debug* print "efficiency for %s %s is %d" %(firstname,lastname,eff)
    player_efficiency.update({myname:round(eff,1)})

def calc_games_played(h,datarow):
    global player_gamesplayed
    datarow = [ 1 if (x == 'NULL' or x == 'N') else x for x in datarow]
    gamesplayed = int(datarow[h['gp']])
    lastname = datarow[h['lastname']]
    firstname = datarow[h['firstname']]
    myname="%s %s" %(firstname,lastname)
    player_efficiency.update({myname:gamesplayed})

for statrow in datafile:
        #print statrow
        calc_efficiency(eff_dict,statrow)
        #calc_games_played(eff_dict,statrow)
#print player_efficiency
## sort player efficiency dictionary by creating tuple
sorted_efficiency_list = sorted(player_efficiency.items(), reverse=True, key = lambda (k,v): v)
#sorted_player_gamesplayed = sorted(player_gamesplayed.items(), reverse=True, key = lambda (k,v): v)

#print sorted_efficiency_list
def print_efficiency_table(topnum,efficiencylist):
    ##top players by efficiency
    print "\nTop %d Most Efficient Players in NBA History, stats collected through 2009" %topnum
    print "-----------------------------------------------------------"
    for i in range(topnum):
        myname = efficiencylist[i][0]
        myefficiency = efficiencylist[i][1]
        print "%s\t%s" %(myefficiency, myname)

def print_topgames_table(topnum,topgameslist):
    ##top players by efficiency
    print "\nTop %d Games played in NBA History, stats collected through 2009" %topnum
    print "-----------------------------------------------------------"
    for i in range(topnum):
        myname = topgameslist[i][0]
        mytopgames = topgameslist[i][1]
        print "%s\t%s" %(mytopgames, myname)
print_efficiency_table(topnum,sorted_efficiency_list)
#print_topgames_table(topnum,sorted_player_gamesplayed)