# A puppet script to install the puppet-lint
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem'
}
