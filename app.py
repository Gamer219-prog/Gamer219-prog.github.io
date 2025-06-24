from flask import Flask, render_template, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_direct_link', methods=['POST'])
def get_direct_link():
    data = request.get_json()
    url = data.get('url', '')
    try:
        # Nutze yt-dlp, um direkte Video-URL zu bekommen (json output)
        result = subprocess.run(
            ['yt-dlp', '-f', 'best', '-j', url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        video_data = json.loads(result.stdout)
        direct_url = video_data['url']  # .googlevideo.com Link
        return jsonify({'success': True, 'direct_url': direct_url})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
