from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/get_link', methods=['POST'])
def get_link():
    data = request.get_json()
    url = data.get("url")

    try:
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
            'format': 'best',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            direct_url = info['url']
            return jsonify({'direct_url': direct_url})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
