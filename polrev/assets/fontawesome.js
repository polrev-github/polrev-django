/*
export interface Config {
  familyPrefix: IconPrefix;
  replacementClass: string;
  autoReplaceSvg: boolean | 'nest';
  autoAddCss: boolean;
  autoA11y: boolean;
  searchPseudoElements: boolean;
  observeMutations: boolean;
  keepOriginalSource: boolean;
  measurePerformance: boolean;
  showMissingIcons: boolean;
}
*/

FontAwesomeConfig = { searchPseudoElements: true }

import { library, dom } from '@fortawesome/fontawesome-svg-core'
/*
import { faSearch, faUserCircle} from "@fortawesome/free-solid-svg-icons";
import { faGithub } from "@fortawesome/free-brands-svg-icons";
library.add(faSearch, faUserCircle, faGithub);

*/
import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'

// Add all icons to the library so you can use it in your page
//library.add(FontAwesomeConfig, fas, far, fab)
library.add(fas, far, fab)

dom.i2svg();
