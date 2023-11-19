from Commands.CodeBreakdownCmds import *
from Commands.FrameworkCmd import *
from Commands.InheritanceOverheadCmds import *
from Commands.MetricsCmd import *
from Commands.TermFrequencyCmds import *
from Commands.CallsToExternalProvidersCmds import *

commands = [EndOfLifeFrameworkCommand(), ForFrequencyCommand(), IfFrequencyCommand(),
            ForEachFrequencyCommand(), WhileFrequencyCommand(), CodeLinesCommand(), CommentLinesCommand(),
            MethodNumberCommand(), ClassNumberCommand(), InterfaceNumberCommand(), InheritanceDeclarationsCommand(),
            ExternalAPICallsCommand(), HttpClientCallsCommand(),
            UsingsNumberCommand(), ClassCouplingListingCommand(), CodeLinesPerFileCommand(),
            CommentLinesPerFileCommand(), CodeSimilarityCommand(),CSFilesCommand()]
