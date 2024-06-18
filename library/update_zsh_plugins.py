#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import re

def parse_and_update_plugins(zshrc_path, new_plugins):
    try:
        with open(zshrc_path, 'r') as f:
            content = f.read()
        
        # Find the existing plugins block
        plugins_block_match = re.search(r'^\s*plugins=\((.*?)\)', content, re.DOTALL | re.MULTILINE)
        
        if plugins_block_match:
            plugins_block = plugins_block_match.group(1)
            current_plugins = [plugin.strip() for plugin in plugins_block.split() if plugin.strip()]
        else:
            current_plugins = []

        # Merge current plugins with new plugins
        all_plugins = sorted(set(current_plugins + new_plugins))
        
        # Replace or add the plugins block
        # Format the new plugins block with each plugin on a new line and proper indentation
        new_plugins_block = "plugins=(\n  " + '\n  '.join(all_plugins) + "\n)"

        if plugins_block_match:
          # Calculate the start position for the replacement
          start_pos = plugins_block_match.start(1)
          # Calculate the end position for the replacement
          end_pos = plugins_block_match.end(1)
          # Replace the content within the parentheses
          updated_content = content[:start_pos] + "\n  " + '\n  '.join(all_plugins) + "\n" + content[end_pos:]
        else:
          # Append the new plugins block at the end if no existing block is found
          updated_content = content + '\n' + new_plugins_block

        # Write back the updated content to .zshrc
        with open(zshrc_path, 'w') as f:
          f.write(updated_content)

        return all_plugins

    except Exception as e:
        raise RuntimeError(f"Failed to update plugins: {str(e)}")

def main():
    module = AnsibleModule(
        argument_spec=dict(
            zshrc_path=dict(type='str', required=True),
            new_plugins=dict(type='list', required=True)
        )
    )

    zshrc_path = module.params['zshrc_path']
    new_plugins = module.params['new_plugins']

    try:
        updated_plugins = parse_and_update_plugins(zshrc_path, new_plugins)
        module.exit_json(changed=True, plugins=updated_plugins)
    except Exception as e:
        module.fail_json(msg=str(e))

if __name__ == '__main__':
    main()
