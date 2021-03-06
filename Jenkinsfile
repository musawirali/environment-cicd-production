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
            sh 'set -x && SNAPSHOT_ID="promotion-"$(date \'+%m%d%Y-%H%M%S\') && INSTANCE_ID=jerry-stage-jx && aws rds create-db-snapshot --region us-west-2 --db-instance-identifier $INSTANCE_ID --db-snapshot-identifier $SNAPSHOT_ID && aws rds wait db-snapshot-completed --region us-west-2 --db-instance-identifier $INSTANCE_ID --db-snapshot-identifier $SNAPSHOT_ID'
            sh 'jx step helm apply'
          }
        }
      }
    }
  }
}
