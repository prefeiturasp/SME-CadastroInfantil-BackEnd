pipeline {
    agent {
        node {
            label 'py-uniformes'
        }
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
        disableConcurrentBuilds()
        skipDefaultCheckout()
    }

    stages {
        stage('CheckOut') {
            steps {
                checkout scm
            }
        }

        stage('Analise codigo') {
            when {
                branch 'homolog'
            }
            steps {
                sh 'sonar-scanner \
                     -Dsonar.projectKey=SME-CadastroInfantil-BackEnd \
                     -Dsonar.sources=. \
                     -Dsonar.host.url=http://sonar.sme.prefeitura.sp.gov.br \
                     -Dsonar.login=3a75f753ee40f65e53142072bf90c9c225ec10e8'
            }
        }

        stage('Deploy DEV') {
            when {
                branch 'develop'
            }
            steps {
                sh 'echo build docker image desenvolvimento'
                // Start JOB para build das imagens Docker e push SME Registry
                script {
                    step([$class: 'RundeckNotifier',
              includeRundeckLogs: true,
              jobId: '351bcf54-2fde-4486-8440-c58a4dc700fc',
              nodeFilters: '',
              //options: """
              //     PARAM_1=value1
              //    PARAM_2=value2
              //     PARAM_3=
              //     """,
              rundeckInstance: 'Rundeck-SME',
              shouldFailTheBuild: true,
              shouldWaitForRundeckJob: true,
              tags: '',
              tailLog: true])
            }

                //Start JOB de deploy Kubernetes
                sh 'echo Deploy ambiente desenvolvimento'
                script {
                    step([$class: 'RundeckNotifier',
              includeRundeckLogs: true,
              jobId: '6fdebb87-1ed1-4703-b8cf-55e6f04a80ca',
              nodeFilters: '',
              //options: """
              //     PARAM_1=value1
              //    PARAM_2=value2
              //     PARAM_3=
              //     """,
              rundeckInstance: 'Rundeck-SME',
              shouldFailTheBuild: true,
              shouldWaitForRundeckJob: true,
              tags: '',
              tailLog: true])
                }
            }
        }

        stage('Deploy homologacao') {
            when {
                branch 'homolog'
            }
            steps {
                timeout(time: 24, unit: 'HOURS') {
                    // telegramSend("${JOB_NAME}...O Build ${BUILD_DISPLAY_NAME} - Requer uma aprovação para deploy !!!\n Consulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)\n")
                    input message: 'Deseja realizar o deploy?', ok: 'SIM', submitter: 'marcos_nastri, calvin_rossinhole, giuseppe_rosa, anderson_morais'
                }
                sh 'echo Deploying ambiente homologacao'

          // Start JOB para build das imagens Docker e push SME Registry

                script {
                    step([$class: 'RundeckNotifier',
              includeRundeckLogs: true,

              //JOB DE BUILD
              jobId: '835f95c0-d659-44ab-beae-01f4aa85a673',
              nodeFilters: '',
              //options: """
              //     PARAM_1=value1
              //    PARAM_2=value2
              //     PARAM_3=
              //     """,
              rundeckInstance: 'Rundeck-SME',
              shouldFailTheBuild: true,
              shouldWaitForRundeckJob: true,
              tags: '',
              tailLog: true])
                }
          //Start JOB deploy Kubernetes

                script {
                    step([$class: 'RundeckNotifier',
              includeRundeckLogs: true,
              jobId: '8147298e-901d-48dc-a5f1-900dd91bf8ba',
              nodeFilters: '',
              //options: """
              //     PARAM_1=value1
              //    PARAM_2=value2
              //     PARAM_3=
              //     """,
              rundeckInstance: 'Rundeck-SME',
              shouldFailTheBuild: true,
              shouldWaitForRundeckJob: true,
              tags: '',
              tailLog: true])
                }
            }
        }

        stage('Deploy PROD') {
            when {
                branch 'master'
            }
            steps {
                timeout(time: 24, unit: 'HOURS') {
                    // telegramSend("${JOB_NAME}...O Build ${BUILD_DISPLAY_NAME} - Requer uma aprovação para deploy !!!\n Consulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)\n")
                    input message: 'Deseja realizar o deploy?', ok: 'SIM', submitter: 'marcos_nastri, calvin_rossinhole, giuseppe_rosa, anderson_morais'
                }
                sh 'echo Build image docker Produção'
          // Start JOB para build das imagens Docker e push SME Registry

                script {
                    step([$class: 'RundeckNotifier',
              includeRundeckLogs: true,

              //JOB DE BUILD
              jobId: '3147f005-2305-4c22-b31e-ed531ea2e332',
              nodeFilters: '',
              //options: """
              //     PARAM_1=value1
              //    PARAM_2=value2
              //     PARAM_3=
              //     """,
              rundeckInstance: 'Rundeck-SME',
              shouldFailTheBuild: true,
              shouldWaitForRundeckJob: true,
              tags: '',
              tailLog: true])
                }
          //Start JOB deploy kubernetes

                script {
                    step([$class: 'RundeckNotifier',
              includeRundeckLogs: true,
              jobId: '6c5e21f0-6150-4d39-b669-97b6f851da0f',
              nodeFilters: '',
              //options: """
              //     PARAM_1=value1
              //    PARAM_2=value2
              //     PARAM_3=
              //     """,
              rundeckInstance: 'Rundeck-SME',
              shouldFailTheBuild: true,
              shouldWaitForRundeckJob: true,
              tags: '',
              tailLog: true])
                }
            }
        }
    }

    post {
        always {
            echo 'One way or another, I have finished'
        }
        success {
            telegramSend("${JOB_NAME}...O Build ${BUILD_DISPLAY_NAME} - Esta ok !!!\n Consulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)\n\n Uma nova versão da aplicação esta disponivel!!!")
        }
        unstable {
            telegramSend("O Build ${BUILD_DISPLAY_NAME} <${env.BUILD_URL}> - Esta instavel ...\nConsulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)")
        }
        failure {
            telegramSend("${JOB_NAME}...O Build ${BUILD_DISPLAY_NAME}  - Quebrou. \nConsulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)")
        }
        changed {
            echo 'Things were different before...'
        }
        aborted {
            telegramSend("O Build ${BUILD_DISPLAY_NAME} - Foi abortado.\nConsulte o log para detalhes -> [Job logs](${env.BUILD_URL}console)")
        }
    }
}
