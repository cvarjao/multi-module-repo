properties(
  [
    [$class: 'BuildConfigProjectProperty', name: '', namespace: '', resourceVersion: '', uid: ''],
    buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '10')),
    [$class: 'RebuildSettings', autoRebuild: false], pipelineTriggers([cron('H H(3-5) * * *')])
  ]
)

stage('cleanup'){
  openshift.withCluster() {
    openshift.selector('all', ['from-pr':'true']).delete();
  }
}
