import time,os,subprocess

class Deploy():

    def frontend(self):
        """To deploy frontend"""
        print('->Deploying frontend...')
        os.system('npm i --prefix frontend/')
        os.system('nohup npm run serve --prefix frontend/ >> frontend/logs/frontend.log &')
        time.sleep(10)
        os.remove('nohup.out')
        print('->Deployed, frontend is running in localhost at port 8080')



    def backend(self):
        """To deploy backend"""
        print('->Deploying backend...')
        os.system('python3 -m backend.main &')
        print('->Deployed, Backend is running in localhost at port 8081.')



if __name__ == "__main__":

    call = Deploy()
    print('->Job Portal App Deployment started..')
    call.backend()
    call.frontend()
    print('->Job Portal App Deployed Successfully :)')
