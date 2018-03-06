properties(
  [
    [$class: 'BuildConfigProjectProperty', name: '', namespace: '', resourceVersion: '', uid: ''],
    buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '10')),
    [$class: 'RebuildSettings', autoRebuild: false],
    parameters([
      string(defaultValue: '', description: 'GutHub webhook payload', name: 'payload')
    ]),
    pipelineTriggers([])
  ]
)


stage('webhook'){
  echo 'Process payload'
}
