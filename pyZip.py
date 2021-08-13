#! python3
#pyZipper.pyw- A python script that compresses files to zip and maintains a local backup too
#Created by Alen Antony
#Version 2.0

import zipfile,os,shutil,logging,sys


'''Automate the files to pick and do this?'''

dir_path=r'C:\Users\alena\OneDrive\Desktop\test' #Path of directory to be compressed 
zipfile_path=r'C:\Users\alena\OneDrive\Desktop\test2\backup.zip'#Path of the compressed file
new_path=r'C:\Users\alena\OneDrive\Desktop\test3' # Path of the new local backup folder
logfile_path=r'C:\Users\alena\OneDrive\Desktop\test2\logfile.txt'# Path of log file

logging.basicConfig(filename=logfile_path, level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.info('Checking for new files in the directory')
if os.listdir(dir_path)==[] :
    logging.info('No new file in the directory,exiting...\n')
    sys.exit()
logging.info('New files found in the directory')

def compress():    
    try:    
        newZip=zipfile.ZipFile(zipfile_path,'a',compression=zipfile.ZIP_DEFLATED)
        logging.info('The compression has started.')
        for  foldername,subfolders,filenames in os.walk(dir_path):
            
            for filename in filenames:
                newZip.write(os.path.join(foldername,filename))
                shutil.move(os.path.join(foldername,filename),os.path.join(new_path,filename))
        newZip.close()
    except Exception as err:
        logging.error('Exception Occurred:'+str(err))
        logging.debug('Compressing the whole backup from '+new_path)
        newZip=zipfile.ZipFile(zipfile_path,'w',compression=zipfile.ZIP_DEFLATED)
        logging.info('The compression has started.')
        for  foldername,subfolders,filenames in os.walk(new_path):
            
            for filename in filenames:
                newZip.write(os.path.join(foldername,filename),os.path.join(dir_path,filename))
            
        newZip.close()
        logging.info('The compression of previously backed up files ended,checking for uncompressed files.')
        if os.listdir(dir_path)==[] :
            logging.info('No uncompressed files found')
        else:
            logging.info('Uncompressed files found,starting compression')
            compress()
    
    
compress()    
logging.info('The compression has ended.')
logging.info('Size of compressed file:'+str(os.path.getsize(zipfile_path)/(1024**3))+" GB\n")










