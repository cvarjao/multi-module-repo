import hudson.model.Result
import jenkins.model.CauseOfInterruption.UserInterruption


def doDeploy=false;
def gitCommitId=''
def isPullRequest=false;

def killOldBuilds() {
  while(currentBuild.rawBuild.getPreviousBuildInProgress() != null) {
    currentBuild.rawBuild.getPreviousBuildInProgress().doKill()
  }
}

pipeline {
    // The options directive is for configuration that applies to the whole job.
    options {
      // Keep 10 builds at a time
      buildDiscarder(logRotator(numToKeepStr:'10'))
      skipDefaultCheckout()
    }
    agent none
    stages {
        stage('checkout') {
            agent any
            steps {
              script {
                killOldBuilds();
              }
              checkout scm
              //sh "git rev-parse HEAD"
              //sh "git ls-remote"
              //sh "git show-ref --head --dereference"
              //sh "git branch"
              //sh "git branch -a"
              //sh "git status"
              //sh "git status -sb"
              //echo "${env}"
              echo 'Building Branch: ' + env.BRANCH_NAME
              echo 'Build Number: ' + env.BUILD_NUMBER
              echo 'CHANGE_ID: ' + env.CHANGE_ID
              echo "CHANGE_TARGET: ${env.CHANGE_TARGET}"
              echo "JOB_NAME: ${env.JOB_NAME}"
              echo "JOB_BASE_NAME: ${env.JOB_BASE_NAME}"
              //timeout(time: 10, unit: 'MINUTES') {
              //  echo "Checkout ..."
              //  echo "Checkout ... Done!"
              //}
              script {
                gitCommitId = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
                isPullRequest=(env.CHANGE_ID != null && env.CHANGE_ID.trim().length()>0)

                echo "gitCommit:${gitCommitId}"
                echo "isPullRequest:${isPullRequest}"

                //def gitRemoteRefBranch = sh(returnStdout: true, script: "git show-ref --head --dereference | grep '${gitCommit}' | cut  -d' ' -f2 | grep 'refs/remotes/origin/' | grep -v 'refs/remotes/origin/pr/'").trim()
                //echo "gitRemoteRefBranch:${gitRemoteRefBranch}"

                //def gitRemoteRefPr = sh(returnStdout: true, script: "git show-ref --head --dereference | grep '${gitCommit}' | cut  -d' ' -f2 | grep 'refs/remotes/origin/' | grep 'refs/remotes/origin/pr/'").trim()
                //echo "gitRemoteRefPr:${gitRemoteRefPr}"


                def scmUrl = scm.getUserRemoteConfigs()[0].getUrl()
                def appName = null;
                def envName = null;
                def buildBranchName = null;

                if (isPullRequest){
                  appName=env.CHANGE_TARGET.split('/')[0]
                  envName='pr'+env.CHANGE_ID;
                  buildBranchName = "refs/pull/${env.CHANGE_ID}/head";
                }else{
                  appName=env.BRANCH_NAME.split('/')[0];
                  envName=env.BRANCH_NAME.substring(appName.length() +1 ).replaceAll('\\Q/\\E','-');
                  buildBranchName = env.BRANCH_NAME;
                }

                def appId = "${appName}-${envName}";

                def baseDeleteLabels=[ 'app-name':appName, 'env-name':envName]
                def baseNewAppLabels=[ 'app':appId, 'env-name':envName, 'build-number':"${env.BUILD_NUMBER}", 'app-name':appName]

                if (isPullRequest){
                  baseNewAppLabels['from-pr']='true'
                }

                echo "scmUrl:${scmUrl}"
                echo "appName:${appName}"
                echo "envName:${envName}"
                echo "appId:${appId}"
                echo "buildBranchName:${buildBranchName}"
                echo "scm.getBranches():${scm.getBranches()}"
                echo "scm.getKey():${scm.getKey()}"
              }
            }
        }
        stage('deploy - DEV') {
            agent any
            when {
                expression { doDeploy == true}
            }
            steps {
              checkout scm
              //sh "git rev-parse HEAD"
              //sh "git ls-remote"
              //sh "git show-ref --head --dereference"
              //sh "git branch"
              //sh "git branch -a"
              //sh "git status"
              //sh "git status -sb"
              //echo "${env}"
              echo 'Building Branch: ' + env.BRANCH_NAME
              echo 'Build Number: ' + env.BUILD_NUMBER
              echo 'CHANGE_ID: ' + env.CHANGE_ID
              echo "CHANGE_TARGET: ${env.CHANGE_TARGET}"
              echo "JOB_NAME: ${env.JOB_NAME}"
              echo "JOB_BASE_NAME: ${env.JOB_BASE_NAME}"
              //timeout(time: 10, unit: 'MINUTES') {
              //  echo "Checkout ..."
              //  echo "Checkout ... Done!"
              //}
              script {
                def gitCommit = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
                def IS_PR=(env.CHANGE_ID != null && env.CHANGE_ID.trim().length()>0)

                echo "gitCommit:${gitCommit}"
                echo "IS_PR:${IS_PR}"

                //def gitRemoteRefBranch = sh(returnStdout: true, script: "git show-ref --head --dereference | grep '${gitCommit}' | cut  -d' ' -f2 | grep 'refs/remotes/origin/' | grep -v 'refs/remotes/origin/pr/'").trim()
                //echo "gitRemoteRefBranch:${gitRemoteRefBranch}"

                //def gitRemoteRefPr = sh(returnStdout: true, script: "git show-ref --head --dereference | grep '${gitCommit}' | cut  -d' ' -f2 | grep 'refs/remotes/origin/' | grep 'refs/remotes/origin/pr/'").trim()
                //echo "gitRemoteRefPr:${gitRemoteRefPr}"


                def scmUrl = scm.getUserRemoteConfigs()[0].getUrl()
                def appName = null;
                def envName = null;
                def buildBranchName = null;

                if (IS_PR){
                  appName=env.CHANGE_TARGET.split('/')[0]
                  envName='pr'+env.CHANGE_ID;
                  buildBranchName = "refs/pull/${env.CHANGE_ID}/head";
                }else{
                  appName=env.BRANCH_NAME.split('/')[0];
                  envName=env.BRANCH_NAME.substring(appName.length() +1 ).replaceAll('\\Q/\\E','-');
                  buildBranchName = env.BRANCH_NAME;
                }

                def appId = "${appName}-${envName}";

                def baseDeleteLabels=[ 'app-name':appName, 'env-name':envName]
                def baseNewAppLabels=[ 'app':appId, 'env-name':envName, 'build-number':"${env.BUILD_NUMBER}", 'app-name':appName]

                if (IS_PR){
                  baseNewAppLabels['from-pr']='true'
                }

                echo "scmUrl:${scmUrl}"
                echo "appName:${appName}"
                echo "envName:${envName}"
                echo "appId:${appId}"
                echo "buildBranchName:${buildBranchName}"
                echo "scm.getBranches():${scm.getBranches()}"
                echo "scm.getKey():${scm.getKey()}"

                //def gitCommit = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()

                openshift.withCluster() { // Use "default" cluster or fallback to OpenShift cluster detection
                    echo "Cancelling Builds"
                    openshift.selector( 'bc', baseDeleteLabels ).narrow('bc').cancelBuild()
                    openshift.selector( 'builds', baseDeleteLabels ).watch {
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
                          if ( it.object().status.phase != "Complete" &&  it.object().status.phase != "Failed") {
                              allDone = false
                          }
                      }
                      return allDone;
                    }

                    echo "Scaling down"
                    openshift.selector( 'dc', baseDeleteLabels ).scale(["--replicas=0"])

                    openshift.selector( 'pods', baseDeleteLabels).watch {
                      echo "pods: ${it.count()}"
                      return it.count() == 0;
                    }

                    echo "Removing"
                    def dcSelector=openshift.selector( 'all', baseDeleteLabels )


                    echo "There are ${dcSelector.count()} deploymentConfig"
                    if (dcSelector.count() !=0 ){
                      def _items=dcSelector.freeze();
                      dcSelector.withEach {
                        echo "Deleted '${it.name()}'"
                      }
                      dcSelector.delete()
                    }

                    //oc get is,bc,svc,routes -l app=backend --export=true --output=json  | out-file ".openshift/resources.json" -encoding utf8
                    //oc new-app 'python:2.7~https://github.com/cvarjao/multi-module-repo.git#frontend/feature/update-greetings' --dry-run=true --output=json | out-file ".openshift/resources.json" -encoding utf8


                    def resourcesAsText=readFile(".openshift/resources.json").replaceAll('\\Q#{app_name}\\E', appId).replaceAll('\\Q#{app_git_url}\\E', scmUrl).replaceAll('\\Q#{app_git_branch}\\E', buildBranchName)
                    echo "${resourcesAsText}"

                    def _newApp=openshift.create(resourcesAsText)

                    _newApp.label(baseNewAppLabels, "--overwrite" )
                    _newApp.label([ 'build-number':"${env.BUILD_NUMBER}" ], "--overwrite" )

                    echo "${_newApp.objects()}"

                    //JOB_NAME
                    echo "Setting-up Route"
                    if (IS_PR){
                      _newApp.label( [ 'pull-request':"${env.CHANGE_ID}" ], "--overwrite" )
                      _newApp.narrow('service').expose()
                      def _svc=_newApp.narrow('service').object()
                      openshift.selector("routes/${_svc.metadata.name}").label(baseNewAppLabels, "--overwrite" )
                    }else{
                      _newApp.narrow('service').expose();
                      def _svc=_newApp.narrow('service').object()
                      openshift.selector("routes/${_svc.metadata.name}").label(baseNewAppLabels, "--overwrite" )
                    }

                    echo "Starting Build"
                    def buildSelector = _newApp.narrow('bc').startBuild("--commit=${buildBranchName}")
                    echo "New build started - ${buildSelector.name()}"
                    buildSelector.logs('-f')

                    echo "${_newApp.count()} has been created"
                    echo "Hello from the project running Jenkins: ${openshift.project()}"

                    echo "Routes:"
                    openshift.selector( 'routes', baseNewAppLabels).withEach {
                      def _o=it.object()
                      echo "${it.name()} - URL: http://${_o.spec.host}"
                    }
                }
              }
              echo "Compiling ..."
              build 'frontend-sit%2Fmaster'
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
