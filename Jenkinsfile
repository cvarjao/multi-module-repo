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
                  openshift.withCluster() { // Use "default" cluster or fallback to OpenShift cluster detection
                      def dcSelector=openshift.selector( 'dc', [ name: 'frontend'] ).describe()
                      echo "There are ${dcSelector.count()} deploymentConfig"
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