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
              timeout(time: 10, unit: 'MINUTES') {
                echo "Checkout ..."
                echo "Checkout ... Done!"
               }
            }
        }
        stage('compile') {
            agent any
            steps {
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