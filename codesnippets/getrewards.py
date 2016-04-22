@api.route('/users/<int:user_id>/rewards/', methods=['GET', 'POST'])
@auth.login_required
def user_rewards(user_id):
    # Get the user account relevant to the user_id parameter
    user = User.query.get(user_id)
    # Verify the logged in user is actually the user or an attached user.
    verify_user(user)

    if request.method == 'GET':
        # Return the user's rewards in JSON format.
        return jsonify(rewards=[r.serialize() for r in user.rewards])