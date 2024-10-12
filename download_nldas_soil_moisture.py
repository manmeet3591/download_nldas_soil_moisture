
# https://disc.gsfc.nasa.gov/datasets/NLDAS_NOAH0125_H_2.0/summary?keywords=soil%20moisture%20gldas
# Go to subset data and select by each year

# We select NLDAS Noah Land Surface Model L4 Hourly 0.125 x 0.125 degree V2.0 (NLDAS_NOAH0125_H 2.0)

!touch .netrc
!echo "machine urs.earthdata.nasa.gov login manmeet.singh@utexas.edu password Austin@123456" >> ~/.netrc
!chmod 0600 .netrc
!touch .urs_cookies

!wget --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --keep-session-cookies --content-disposition  https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHH.07/2000/153/3B-HHR.MS.MRG.3IMERG.20000601-S000000-E002959.0000.V07B.HDF5

# Use -i name of the file with links.txt to download multiple files
