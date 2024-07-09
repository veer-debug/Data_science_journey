private fun playRecordedAudio() {
        mediaPlayer = MediaPlayer().apply {
            try {
                setDataSource(outputFilePath)
                prepare()
                start()
            } catch (e: IOException) {
                e.printStackTrace()
            }
        }
    }