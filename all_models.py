# coding=utf-8
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Library to import and register all TLP models."""

from fm4tlp.models import dyrep
from fm4tlp.models import edgebank
from fm4tlp.models import jodie
from fm4tlp.models import tgn

# keep-sorted start
DyRep = dyrep.DyRep
EdgeBank = edgebank.EdgeBank
JODIE = jodie.JODIE
TGN = tgn.TGN
# keep-sorted end
