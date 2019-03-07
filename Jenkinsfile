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
            sh 'sops -d secrets.enc.yaml > secrets.dec.yaml'
            sh 'python encrypt64.py'
            sh 'pip install awscli'
            sh 'sops -d awscredentials.enc.env > awscredentials.env'
            sh 'source awscredentials.env; set -x && aws rds create-db-snapshot --db-instance-identifier jerry-stage-jx --db-snapshot-identifier ${echo "promotion@$(date \'+%m%d%Y-%H:%M:%S\')"}'
            sh 'jx step helm apply'
          }
        }
      }
    }
  }
}
