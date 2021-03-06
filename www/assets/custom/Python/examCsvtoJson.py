import csv
import json

# Open the CSV
f = open( 'exams.csv', 'rU' )
# Change each fieldname to the appropriate field name. I know, so difficult.
reader = csv.DictReader( f, fieldnames = ( "module","type","date","time","duration" ))
# Parse the CSV into JSON
out = json.dumps( [ row for row in reader ] )
print ("JSON parsed!")
# Save the JSON
f = open( 'exams.json', 'w')
f.write(out)
print ("JSON saved!")
