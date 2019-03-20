pipeline {
  options {
    disableConcurrentBuilds()
  }
  agent {
    label "jenkins-maven"
  }
  environment {
    DEPLOY_NAMESPACE = "jx-production"
  }
  stages {
    stage('Validate Environment') {
      steps {
        container('maven') {
          dir('env') {
            sh 'jx step helm build'
          }
        }
      }
    }
    stage('Update Environment') {
      when {
        branch 'master'
      }
      steps {
        container('maven') {
          dir('env') {
            sh 'wget https://github.com/mozilla/sops/releases/download/3.2.0/sops-3.2.0-1.x86_64.rpm && yum install -y sops-3.2.0-1.x86_64.rpm && rm sops-3.2.0-1.x86_64.rpm'
            sh 'sh decode_secrets.sh'
            sh 'python encrypt64.py'
            sh 'jx step helm apply'
          }
        }
      }
    }
  }
}
