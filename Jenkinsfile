pipeline {
    // The options directive is for configuration that applies to the whole job.
    options {
      // Keep 10 builds at a time
      buildDiscarder(logRotator(numToKeepStr:'10'))
    }
    agent none 
    stages {
        stage('checkout') {
            agent any
            steps {
              echo "${env}"
              echo 'Building Branch: ' + env.BRANCH_NAME
              echo 'Build Number: ' + env.BUILD_NUMBER
              echo 'CHANGE_ID: ' + env.CHANGE_ID
              echo "CHANGE_TARGET: ${env.CHANGE_TARGET}"
              echo "JOB_NAME: ${env.JOB_NAME}"
              echo "JOB_BASE_NAME: ${env.JOB_BASE_NAME}"
              timeout(time: 10, unit: 'MINUTES') {
                echo "Checkout ..."
                echo "Checkout ... Done!"
               }
            }
        }
        stage('compile') {
            agent any
            steps {
                script {
                  def scmUrl = scm.getUserRemoteConfigs()[0].getUrl()
                  def appName = env.BRANCH_NAME.split('/')[0]
                  echo "scmUrl:${scmUrl}"
                  echo "appName:${appName}"
                  echo "scm.getBranches():${scm.getBranches()}"
                  echo "scm.getKey():${scm.getKey()}"
                  
                  //def gitCommit = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
                  
                  openshift.withCluster() { // Use "default" cluster or fallback to OpenShift cluster detection
                      
                      echo "Cancelling Builds"
                      openshift.selector( 'bc', [ 'app':appName] ).narrow('bc').cancelBuild()
                      openshift.selector( 'builds', [ 'app':appName] ).watch {
                        echo "builds: ${it.count()}"
                        if ( it.count() == 0 ) return true

                        // A robust script should not assume that only one build has been created, so
                        // we will need to iterate through all builds.
                        def allDone = true
                        it.withEach {
                            // 'it' is now bound to a Selector selecting a single object for this iteration.
                            // Let's model it in Groovy to check its status.
                            def buildModel = it.object()
                            echo "${it.name()}:status.phase: ${it.object().status.phase}"
                            if ( it.object().status.phase != "Complete" ) {
                                allDone = false
                            }
                        }
                        return allDone;
                      }
                      
                      
                      
                      echo "Scaling down"
                      openshift.selector( 'dc', [ 'app':appName] ).scale(["--replicas=0"])
                      
                      openshift.selector( 'pods', [ 'app':appName] ).watch {
                        echo "pods: ${it.count()}"
                        return it.count() == 0;
                      }
                      
                      echo "Removing"
                      def dcSelector=openshift.selector( 'all', [ 'app':appName] )
                      
                      
                      echo "There are ${dcSelector.count()} deploymentConfig"
                      if (dcSelector.count() !=0 ){
                        def _items=dcSelector.freeze();                        
                        dcSelector.withEach {
                          echo "Deleted '${it.name()}'"
                        }
                        dcSelector.delete()
                      }
                      
                      def _newApp=openshift.newApp('python:2.7~https://github.com/OpenShiftDemos/os-sample-python.git', "--name=${appName}", '-l', "app=${appName}")
                      _newApp.withEach {
                          echo "Created '${it.name()}'"
                      }
                      
                      _newApp.label( [ 'jenkins-build-number':"${env.BUILD_NUMBER}" ], "--overwrite" )
                      _newApp.narrow('service').expose('-l', "app=${appName}");
                      _newApp.narrow('bc').logs('-f')
                      
                      echo "${_newApp.count()} has been created"
                      
                      echo "Hello from the project running Jenkins: ${openshift.project()}"
                  }
                }
                echo "Compiling ..."
                
                echo "Compiling ... Done!"
            }
        }
        stage('testing') {
            agent any
            steps {
                echo "Testing ..."
                echo "Testing ... Done!"
            }
        }
        stage('packaging') {
            agent any
            steps {
                echo "Packaging ..."
                echo "Packaging ... Done!"
            }
        }
        stage('publishing') {
            agent any
            steps {
                echo "Publishing ..."
                echo "Publishing ... Done!"
            }
        }
    }
}