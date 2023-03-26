#! /usr/bin/bash

curl https://www.coingecko.com/en/coins/ethereum/historical_data#panel -o output.csv 
html2text output.csv > parsed_data.csv 
sed -n '/(Historical Data)/,$p' parsed_data.csv > price_data.csv 
sed -n '/Date/,$p' price_data.csv > price_data2.csv  
sed -i '/^Want/q' price_data2.csv 
sed -i '$ d' price_data2.csv 
sed -i '1d' price_data2.csv
sed -i '1iDate Market_Cap Volume Open Close' price_data2.csv

mv price_data2.csv data_eth.csv
rm output.csv 
rm parsed_data.csv 
rm price_data.csv 

curl https://www.coingecko.com/en/coins/xrp/historical_data#panel -o output.csv 
html2text output.csv > parsed_data.csv 
sed -n '/(Historical Data)/,$p' parsed_data.csv > price_data.csv 
sed -n '/Date/,$p' price_data.csv > price_data2.csv  
sed -i '/^Want/q' price_data2.csv 
sed -i '$ d' price_data2.csv 
sed -i '1d' price_data2.csv
sed -i '1iDate Market_Cap Volume Open Close' price_data2.csv

mv price_data2.csv data_xrp.csv
rm output.csv 
rm parsed_data.csv 
rm price_data.csv 


echo "Scrap done"
 
