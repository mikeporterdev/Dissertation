# Test no authentication details
child = create_child(self)
rv = self.client.get('/api/users/' + child['id'] + '/')
self.assert401(rv)